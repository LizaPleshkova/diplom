import { createApp } from 'vue'
import App from './App.vue'
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'
import router from './router/index'



createApp(App).use(router).mount('#app')
// const app = new Vue({
//     router
//   }).$mount('#app')