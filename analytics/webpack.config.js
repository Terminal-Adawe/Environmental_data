const path = require('path');

module.exports = {
  entry: {
    index: './assets/index.js',  // path to our input file
    report: './assets/reportGraphs.js',
  },
  output: {
    filename: '[name]-bundle.js',  // output bundle file name
    path: path.resolve(__dirname, './static'),  // path to our Django static directory
  },
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: /node_modules/,
        loader: "babel-loader",
        options: { presets: ["@babel/preset-env", "@babel/preset-react"] }
      },
      {
        test: /\.css$/i,
        use: ["to-string-loader", "css-loader"],
      },
    ]
  }
};
