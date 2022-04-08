import { createStore } from "vuex";
// import CinemaService from "../services/DataService";
import cinemaModule from "../store/modules/cinema.js";
import movieModule from "../store/modules/movie.js";
import authModule from "../store/modules/auth.js";
import movieSessionModule from "../store/modules/movie_session.js";

const store = createStore({
  modules: {
    cinemaModule,
    movieModule,
    authModule,
    movieSessionModule
    },
});

export default store;
