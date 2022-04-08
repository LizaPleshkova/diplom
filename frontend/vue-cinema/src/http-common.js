import axios from "axios";
// import store from '@/store/index.js'

const HTTP = axios.create({
  baseURL: `http://localhost:8000/api/`,
  headers: {
    "Content-type": "application/json",
    'Authorization': "Bearer " + localStorage.getItem('token')
  },
});

export const HTTP_USER = axios.create({
  baseURL: `http://localhost:8000/client/`,
  headers: {
    "Content-type": "application/json",
    // 'Authorization': "Bearer " + this.$store.state.authModule.user.accessToken
  },
});

// // this.$store.getters.accessToken;
// console.log($store.getters.accessToken)
// if ($store.getters.accessToken) {
//   axios.defaults.headers.common['Authorization'] = "Bearer " + this.$store.state.authModule.user.accessToken;
// } else {
//   axios.defaults.headers.common['Authorization'] = "";
// }

export default HTTP;
