import { createApp } from "vue";
import  Vue  from  'vue'
import App from "./App.vue";
import router from "./router/index";
import store from "./store/index";
import "bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";

const  accessToken  =  localStorage.getItem('access_token')

if (accessToken) {
    Vue.prototype.$http.defaults.headers.common['Authorization'] =  accessToken
}

createApp(App).use(router).use(store).mount("#app");
