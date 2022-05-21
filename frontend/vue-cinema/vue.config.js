module.exports = {
    devServer: {
      host: 'localhost',
    },
    chainWebpack: config => {
      config.module.rules.delete('eslint');
  }
    
  };