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
          900: '#0F2338',
          800: '#16324F', // Primary Deep Navy
          700: '#1E4368',
          600: '#27527D',
        },
        medblue: {
          DEFAULT: '#2F6F8F', // Medical Blue
          light: '#E8F0F3',   // Mist Blue
          hover: '#245A75',
          dark: '#1D455A',
        },
        teal: {
          DEFAULT: '#4F8A8B', // Muted Teal
          light: '#EDF5F5',
          dark: '#3B6B6C',
        },
        sage: {
          DEFAULT: '#7C9A92', // Sage Green
          light: '#E7EFEB',   // Pale Sage
          dark: '#5F7C74',
        },
        ivory: {
          DEFAULT: '#F7F5EF', // Main Background
          dark: '#EEEBE1',
        },
        surface: '#FCFBF8',   // Card Surface
        charcoal: '#263238',  // Text Charcoal
        slateText: '#65727E', // Secondary Text
        beige: '#EDE7DC',      // Warm Beige Accent
        borderLine: '#DCE3E2', // Clinical divider line
        status: {
          healthy: '#2E7D32',
          healthyBg: '#EAF4EC',
          healthyBorder: '#C8E6C9',
          warning: '#C97A2B',
          warningBg: '#FDF5EC',
          warningBorder: '#FFE0B2',
          critical: '#B33939',
          criticalBg: '#FDF0F0',
          criticalBorder: '#FFCDD2',
          info: '#2F6F8F',
          infoBg: '#EEF5F8',
          infoBorder: '#B3D4E5',
        }
      },
      fontFamily: {
        sans: ['Inter', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'Roboto', 'sans-serif'],
        serif: ['"Cormorant Garamond"', 'Georgia', 'serif'],
        display: ['"Libre Baskerville"', 'Georgia', 'serif'],
      },
      boxShadow: {
        'subtle': '0 1px 3px 0 rgba(22, 50, 79, 0.04), 0 1px 2px -1px rgba(22, 50, 79, 0.02)',
        'medical': '0 4px 18px 0 rgba(22, 50, 79, 0.05), 0 1px 3px 0 rgba(22, 50, 79, 0.03)',
        'elevated': '0 10px 30px -4px rgba(22, 50, 79, 0.08), 0 4px 10px -2px rgba(22, 50, 79, 0.04)',
      },
      borderRadius: {
        'card': '14px',
        'btn': '9px',
      }
    },
  },
  plugins: [],
}
