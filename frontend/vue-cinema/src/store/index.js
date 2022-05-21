import { createStore } from "vuex";
// import CinemaService from "../services/DataService";
import cinemaModule from "../store/modules/cinema.js";
import movieModule from "../store/modules/movie.js";
import authModule from "../store/modules/auth.js";
import movieSessionModule from "../store/modules/movie_session.js";
import commentsModule from "../store/modules/comments.js";
import profileModule from "../store/modules/profile.js";

const store = createStore({
  modules: {
    cinemaModule,
    movieModule,
    authModule,
    movieSessionModule,
    commentsModule,
    profileModule
    },
});

export default store;
