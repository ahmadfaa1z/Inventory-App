/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['../templates/*.html',
            '../static/node_modules/tw-elements/dist/js/**/*.js',
            '../static/js/*.js'],
  theme: {
    extend: {},
  },
  plugins: [require('tw-elements/dist/plugin')],
}
