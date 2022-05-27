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
        state.user.refreshToken = localStorage.getItem("refreshToken");
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
    setAccessToken(state, accessToken) {
      state.user.accessToken = accessToken;
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
    },
    getToken(state){
      return state.accessToken;
    },
    getRefreshToken(state){
      return state.refreshToken;
    }
  },
  actions: {
    userLogout(context) {
        if (context.getters.loggedIn){
          context.commit('removeToken')
          localStorage.removeItem('token');
          localStorage.removeItem('refreshToken');
        }
      },
      refreshToken: async ({ state, commit }) => {
        console.log('from store ', state.user.refreshToken)

        const refreshUrl = "http://localhost:8000/client/api/token/refresh/";
        try {
          await axios
            .post(refreshUrl, { 'refresh': state.user.refreshToken})
            .then(response => {
              console.log('from store 2', response)
              if (response.status === 200) {
                commit("setAccessToken", response.data.access);
              }
            return response.data
            });
        } catch (e) {
          console.log(e.response);
        }
      },
  },
};

export default authModule;
