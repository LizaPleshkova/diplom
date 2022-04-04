// import CinemaService from "./services/DataService";
import MovieService from "../../services/MovieService";

const movieModule = {
  actions: {
    async getMovies(context) {
      MovieService.getMovies().then((movies) => {
        context.commit("set_movies", movies);
      });
    },
    async getMovie(context, pk) {
      MovieService.getMovie(pk).then((movie) => {
        context.commit("set_movie", movie);
      });
    },
  },
  mutations: {
    set_movies(state, movies) {
      state.movies = movies;
    },
    set_movie(state, movie) {
      state.movie = movie;
    },
  },
  state: {
    movies: [],
    movie: null,
  },
  getters: {
    allMovies(state) {
      return state.movies;
    },
    currentMovie(state) {
      return state.movie;
    },
  },
};

export default movieModule;
