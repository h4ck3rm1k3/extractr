var ManifestPlugin = require('webpack-manifest-plugin');
//var ManifestRevisionPlugin = require('manifest-revision-webpack-plugin');

module.exports = {
  entry: "./static/sw/index.js",

  //                 ./static/compare/compare.js
  //               ./static/compare/overpass_client.js  
    output: {
        path: './static/compare/',
      publicPath: "/static/",
        filename: "bundle.js"
    },

  plugins: [
      new ManifestPlugin( {
        fileName: 'compare-manifest.json',
        ///basePath: '/static/compare/',
        publicPath: "/static/",
      }
      ),

    // new ManifestRevisionPlugin(path.join('static', 'manifest2.json'), {
    //     rootAssetPath: rootAssetPath,
    //     ignorePaths: ['/stylesheets', '/javascript']
    // })

    ]
};