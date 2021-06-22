const path = require('path');

module.exports = {
  entry: {
    index: './assets/index.js',  // path to our input file
    report: './assets/reportGraphs.js',
    graphbuilder: './assets/graphBuilder.js',
    notifications: './assets/notifications.js',
    task_scheduler: './assets/task_scheduler.js',
    table_builder: './assets/table_builder.js',
    custom_tables: './assets/custom_tables.js',
    custom_table: './assets/custom_table.js',
    report_list: './assets/reports.js',
    add_report: './assets/addReport.js',
    save_button: './assets/saveBtn.js'
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
