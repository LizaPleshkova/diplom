import axios from "axios";
import store from "./store/index";
import router from "./router/index.js";

const HTTP = axios.create({
  baseURL: `http://localhost:8000/api/`,
  headers:  {
    "Content-type": "application/json",
  'Authorization': "Bearer " + localStorage.getItem('token')
}
  
});

export const HTTP_USER = axios.create({
  baseURL: `http://localhost:8000/client/`,
});

// HTTP.interceptors.request.use(function (config) {
//   console.log('works', config)
//   const  accessToken  =  localStorage.getItem('token')
//   config.headers.common["Authorization"] =  'Bearer ' + accessToken;
//   // config.headers.common["Content-type"] = 'application/json';
//   // Do something before request is sent
//   return config;
// }, function (error) {
//   // Do something with request error
//   return Promise.reject(error);
// });

// HTTP.interceptors.response.use(function (response) {
//   // Any status code that lie within the range of 2xx cause this function to trigger
//   // Do something with response data
//   return response;
// }, async function (error) {
//   console.log(error)
//   // Any status codes that falls outside the range of 2xx cause this function to trigger
//   // Do something with response error
//   if (error.response.status === 401) {
//     console.log('store.getters', store )
//     console.log('store.getters', store.state.authModule)
//     // const authData = store.authModule.getters.getToken;
//     const user = {
//       access_token: localStorage.getItem('token'),
//       refresh_token: localStorage.getItem('refreshToken'),
//     };
//     var dat = await store.dispatch("refreshToken");
//     console.group('dat',dat)
//     // error.config.headers[
//     //   "Authorization"
//     // ] = `bearer ${response.data.access_token}`;
//     return axios(error.config);
//   } else {
//     return Promise.reject(error);
//   }
//   // return Promise.reject(error);
// });

export default HTTP;