/**
 * MedPredict AI — Authentication & Role Switcher Context
 */

import React, { createContext, useContext, useState, useEffect, ReactNode } from 'react';
import { User } from '../types';
import { api } from '../services/api';

interface AuthContextType {
  user: User | null;
  token: string | null;
  activeRole: string;
  setActiveRole: (role: string) => void;
  login: (username: string, password: string) => Promise<void>;
  logout: () => void;
  isLoading: boolean;
  hasRole: (role: string) => boolean;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export const AuthProvider: React.FC<{ children: ReactNode }> = ({ children }) => {
  const [user, setUser] = useState<User | null>(null);
  const [token, setToken] = useState<string | null>(localStorage.getItem('medpredict_access_token'));
  const [activeRole, setActiveRoleState] = useState<string>(
    localStorage.getItem('medpredict_active_role') || 'patient'
  );
  const [isLoading, setIsLoading] = useState<boolean>(true);

  const setActiveRole = (role: string) => {
    setActiveRoleState(role);
    localStorage.setItem('medpredict_active_role', role);
  };

  const loadCurrentUser = async () => {
    try {
      if (token) {
        const currentUser = await api.auth.getMe();
        setUser(currentUser);
        // Default active role to the highest available role if not set
        if (currentUser.roles && currentUser.roles.length > 0) {
          const userRoleNames = currentUser.roles.map((r) => r.name.toLowerCase());
          const stored = localStorage.getItem('medpredict_active_role');
          if (!stored || !userRoleNames.includes(stored)) {
            const prioritized = ['admin', 'doctor', 'data_scientist', 'researcher', 'patient'];
            const firstMatch = prioritized.find((r) => userRoleNames.includes(r)) || userRoleNames[0];
            setActiveRole(firstMatch);
          }
        }
      } else {
        setUser(null);
      }
    } catch (err) {
      console.error('Failed to load authenticated user profile', err);
      logout();
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    loadCurrentUser();
  }, [token]);

  const login = async (username: string, password: string) => {
    setIsLoading(true);
    try {
      const params = new URLSearchParams();
      params.append('username', username);
      params.append('password', password);

      const authData = await api.auth.login(params);
      localStorage.setItem('medpredict_access_token', authData.access_token);
      localStorage.setItem('medpredict_refresh_token', authData.refresh_token);
      setToken(authData.access_token);
    } catch (err) {
      setIsLoading(false);
      throw err;
    }
  };

  const logout = () => {
    localStorage.removeItem('medpredict_access_token');
    localStorage.removeItem('medpredict_refresh_token');
    localStorage.removeItem('medpredict_active_role');
    setToken(null);
    setUser(null);
    setActiveRoleState('patient');
    setIsLoading(false);
  };

  const hasRole = (role: string): boolean => {
    if (!user || !user.roles) return false;
    return user.roles.some((r) => r.name.toLowerCase() === role.toLowerCase());
  };

  return (
    <AuthContext.Provider
      value={{
        user,
        token,
        activeRole,
        setActiveRole,
        login,
        logout,
        isLoading,
        hasRole,
      }}
    >
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = (): AuthContextType => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
};
