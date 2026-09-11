/**
 * MedPredict AI — Elegant Medical Statistic Card Component
 * Warm White (#FCFBF8) surface, thin border, subtle elevation, restrained clinical typography
 */

import React from 'react';
import { LucideIcon, TrendingUp, TrendingDown, Minus } from 'lucide-react';

interface StatCardProps {
  label: string;
  value: string | number;
  change?: string;
  changeType?: 'positive' | 'negative' | 'neutral';
  subtext?: string;
  icon: LucideIcon;
  accentColor?: string;
}

export const StatCard: React.FC<StatCardProps> = ({
  label,
  value,
  change,
  changeType = 'neutral',
  subtext,
  icon: Icon,
}) => {
  return (
    <div className="bg-surface rounded-card p-5 border border-borderLine shadow-medical card-hover flex flex-col justify-between">
      <div className="flex items-center justify-between">
        <span className="text-xs font-semibold text-slateText tracking-wide uppercase font-sans">
          {label}
        </span>
        <div className="w-8 h-8 rounded-lg bg-medblue-light flex items-center justify-center text-medblue">
          <Icon className="w-4 h-4" />
        </div>
      </div>

      <div className="mt-3">
        <div className="text-2xl lg:text-3xl font-bold text-navy-800 tracking-tight font-sans">
          {value}
        </div>
      </div>

      <div className="mt-3 pt-3 border-t border-borderLine/50 flex items-center justify-between text-xs">
        {change && (
          <div className="flex items-center space-x-1">
            {changeType === 'positive' && (
              <span className="flex items-center text-status-healthy font-semibold">
                <TrendingUp className="w-3.5 h-3.5 mr-0.5" />
                {change}
              </span>
            )}
            {changeType === 'negative' && (
              <span className="flex items-center text-status-critical font-semibold">
                <TrendingDown className="w-3.5 h-3.5 mr-0.5" />
                {change}
              </span>
            )}
            {changeType === 'neutral' && (
              <span className="flex items-center text-slateText font-medium">
                <Minus className="w-3.5 h-3.5 mr-0.5" />
                {change}
              </span>
            )}
          </div>
        )}
        {subtext && (
          <span className="text-[11px] text-slateText truncate ml-auto">
            {subtext}
          </span>
        )}
      </div>
    </div>
  );
};
