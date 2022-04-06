// import CinemaService from "./services/DataService";
import MovieService from "../../services/MovieService";
// import axios from 'axios';

const movieModule = {
  actions: {
    async getMovies(context) {
      MovieService.getMovies().then((movies) => {
        context.commit("set_movies", movies);
      });
    },
    async getMovie(context, pk, filters=null) {
      if ( filters == null){
         MovieService.getMovie(pk).then((movie) => {
        context.commit("set_movie", movie);
      });
      }
    },
    async getFilterMovies(context, filters) {
      console.log('from vuex', filters);
      MovieService.getFilterMovies(filters).then((movies) => {
        context.commit("set_movies", movies);
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
