const path = require("path");

module.exports = {
  entry: "./_webpack/main.js",
  output: {
    filename: "main.js",
    path: path.resolve(__dirname, "javascript"),
  },
  mode: process.env.NODE_ENV || "development",
};
