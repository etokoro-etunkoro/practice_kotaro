// webpack.config.js
const path = require('path');
const ESLintPlugin = require('eslint-webpack-plugin');

module.exports = {
  mode: 'development',
  entry: './src/index.js',
  output: {
    path: path.resolve(__dirname, 'public/js'),
    filename: 'app.js',
    publicPath: '/js/',
    clean: true,
  },
  devtool: 'inline-source-map',
  devServer: {
    static: { directory: path.resolve(__dirname, 'public') },
    port: 8080,
    historyApiFallback: true,
    hot: true,
    open: true,
  },
  plugins: [
    new ESLintPlugin({
      extensions: ['js', 'jsx'],   // これだけでOK（overrideConfigFileは削除）
    }),
  ],
  module: {
    rules: [
      { test: /\.css$/, use: ['style-loader', 'css-loader'] },
      { test: /\.js$/, exclude: /node_modules/, loader: 'babel-loader' },
    ],
  },
  resolve: { extensions: ['.js', '.jsx'] },
};
