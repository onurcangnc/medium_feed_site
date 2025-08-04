module.exports = {
  content: [
    "./templates/**/*.html",
    "./templates/**/*.j2",
    "./templates/**/*.html.j2",
    "./output/**/*.html",
    './**/*.html',
    './**/*.js',
    './**/*.md',
    './**/*.json',
  ],
  theme: {
    extend: {},
  },
  plugins: [
  require('@tailwindcss/typography'),
  require('@tailwindcss/aspect-ratio'),
  require('@tailwindcss/forms'),
  ]
}
