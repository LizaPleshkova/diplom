import { createStore } from "vuex";
// import CinemaService from "../services/DataService";
import cinemaModule from "../store/modules/cinema.js";
import movieModule from "../store/modules/movie.js";


const store = createStore({
  modules: {
    cinemaModule,
    movieModule
  },
});

export default store;
