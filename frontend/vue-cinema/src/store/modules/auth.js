// import AuthService from '@/services/user/AuthService.js';

// const user = JSON.parse(localStorage.getItem('user'));

// const initialState = user
//   ? { status: { loggedIn: true }, user }
//   : { status: { loggedIn: false }, user: null };
// console.log(initialState);

export const authModule = {
  state: {
    user: {
      accessToken: "",
      refreshToken: "",
      isAuthenticated: false,
    },
  },
  mutations: {
    initializeStore(state) {
      if (localStorage.getItem("token")) {
        state.user.accessToken = localStorage.getItem("token");
        state.user.isAuthenticated = true;
      } else {
        state.user.accessToken = "";
        state.user.refreshToken = "";
        state.user.isAuthenticated = false;
      }
    },
    setToken(state, accessToken, refreshToken) {
      state.user.accessToken = accessToken;
      state.user.refreshToken = refreshToken;
      state.user.isAuthenticated = true;
    },
    removeToken(state) {
      state.user.accessToken = "";
      state.user.refreshToken = "";
      state.user.isAuthenticated = false;
      
      // localStorage.removeItem('username')
    },
  },
  getters:{
    loggedIn(state){
      return state.isAuthenticated = true
    }
  },
  actions: {
    userLogout(context) {
        if (context.getters.loggedIn){
          context.commit('removeToken')
          localStorage.removeItem('token');
        }
      }
  },
};

export default authModule;
