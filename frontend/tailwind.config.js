module.exports = {
  content: [
    "../homedecor/templates/**/*.html",
    "../homedecor/*/templates/**/*.html",
    "../homedecor/**/templates/**/**/*.html", // for deeply nested app templates if any
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
