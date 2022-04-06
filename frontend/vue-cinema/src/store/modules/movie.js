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
    async getMovie(context, pk) {
      MovieService.getMovie(pk).then((data) => {

        console.log('only movie',data.movie);
        console.log('only ms',data.movie_sessions);
        
        context.commit("set_movie", data.movie);
        context.commit("set_movie_session", data.movie_sessions);
      });
    },
    async getFilterMovies(context, filters) {
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
    set_movie_session(state, movie_s) {
      state.movie_session = movie_s;
    },
  },
  state: {
    movies: [],
    movie: null,
    movie_session: []
  },
  getters: {
    allMovies(state) {
      return state.movies;
    },
    currentMovie(state) {
      return state.movie;
    },
    movieSession(state) {
      console.log(state.movie_session)
      return state.movie_session;
    },
  },
};

export default movieModule;
