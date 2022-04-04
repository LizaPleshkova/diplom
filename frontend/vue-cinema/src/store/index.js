import { createStore } from "vuex";
// import CinemaService from "../services/DataService";
import cinemaModule from "../store/modules/cinema.js";
import movieModule from "../store/modules/movie.js";
import authModule from "../store/modules/auth.js";

const store = createStore({
  modules: {
    cinemaModule,
    movieModule,
    authModule
  },
});

export default store;
