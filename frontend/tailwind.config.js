/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        navy: {
          900: '#0F172A', // Slate 900
          800: '#1E293B', // Slate 800 (Clean Clinical Navy)
          700: '#334155', // Slate 700
          600: '#475569', // Slate 600
        },
        medblue: {
          DEFAULT: '#0284C7', // Clinical Medical Blue (Sky 600)
          light: '#F0F9FF',   // Subtle Blue Tint
          hover: '#0369A1',   // Sky 700
          dark: '#0C4A6E',    // Sky 900
        },
        teal: {
          DEFAULT: '#0D9488', // Teal 600
          light: '#F0FDFA',   // Teal 50
          dark: '#115E59',    // Teal 800
        },
        sage: {
          DEFAULT: '#16A34A', // Clinical Green (Green 600)
          light: '#F0FDF4',   // Light Green Tint
          dark: '#15803D',    // Green 700
        },
        ivory: {
          DEFAULT: '#F8FAFC', // Crisp Clean Clinical Background (Slate 50)
          dark: '#F1F5F9',    // Slate 100
        },
        surface: '#FFFFFF',   // Pure Crisp Medical Surface
        charcoal: '#0F172A',  // High-Readability Clinical Text (Slate 900)
        slateText: '#64748B', // Neutral Secondary Text (Slate 500)
        beige: '#F1F5F9',      // Subtle Slate Divider
        borderLine: '#E2E8F0', // Crisp 1px Medical Border (Slate 200)
        status: {
          healthy: '#16A34A',      // Authentic Clinical Green
          healthyBg: '#F0FDF4',
          healthyBorder: '#BBF7D0',
          warning: '#D97706',      // Authentic Amber
          warningBg: '#FFFBEB',
          warningBorder: '#FDE68A',
          critical: '#DC2626',     // Authentic Crimson
          criticalBg: '#FEF2F2',
          criticalBorder: '#FECACA',
          info: '#0284C7',         // Clinical Sky Blue
          infoBg: '#F0F9FF',
          infoBorder: '#BAE6FD',
        }
      },
      fontFamily: {
        sans: ['Inter', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'Roboto', 'sans-serif'],
        serif: ['"Cormorant Garamond"', 'Georgia', 'serif'],
        display: ['"Libre Baskerville"', 'Georgia', 'serif'],
      },
      boxShadow: {
        'subtle': '0 1px 2px 0 rgba(0, 0, 0, 0.04)',
        'medical': '0 1px 3px 0 rgba(0, 0, 0, 0.05), 0 1px 2px -1px rgba(0, 0, 0, 0.05)',
        'elevated': '0 4px 6px -1px rgba(0, 0, 0, 0.07), 0 2px 4px -2px rgba(0, 0, 0, 0.05)',
      },
      borderRadius: {
        'card': '8px',
        'btn': '6px',
      }
    },
  },
  plugins: [],
}
