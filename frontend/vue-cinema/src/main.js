import { createApp } from "vue";
import  Vue  from  'vue'
import App from "./App.vue";
import router from "./router/index";
import store from "./store/index";
// Import Bootstrap an BootstrapVue CSS files (order is important)
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
// const  accessToken  =  localStorage.getItem('accessToken')

// if (accessToken) {
//     Vue.prototype.$http.defaults.headers.common['Authorization'] =  'Bearer ' + accessToken;
// }

createApp(App).use(router).use(store).mount("#app");
