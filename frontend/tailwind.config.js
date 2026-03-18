/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        blurple: '#5865F2',
        darker: '#36393f',
        darkest: '#2f3136',
      }
    },
  },
  plugins: [],
}
