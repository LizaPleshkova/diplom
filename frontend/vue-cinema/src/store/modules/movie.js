// import CinemaService from "./services/DataService";
import MovieService from "../../services/MovieService";
// import axios from 'axios';

// function update_date_ms(movie_sessions){
//   for(var ms in movie_sessions){
//     console.log(ms);
//       let new_date = new Date( ms.datetime_session )
//       console.log(ms.datetime_session);
//       ms.datetime_session = new_date.toLocaleString("en-US");
//   }
// }

const movieModule = {
  actions: {
    async getMovies(context) {
      MovieService.getMovies().then((movies) => {
        context.commit("set_movies", movies);
      });
    },
    async getMovie(context, pk) {
      MovieService.getMovie(pk).then((data) => {
        console.log("only movie", data.movie);
        console.log("only ms", data.movie_sessions);

        for (var ms_key in data.movie_sessions) {
          let movie_sessions = data.movie_sessions[ms_key];
          let new_date = new Date(movie_sessions["datetime_session"]);
          var date = new_date.toLocaleDateString('en', { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' })
          var time = new_date.toLocaleTimeString('en-US')
          movie_sessions["datetime_session"] = {
            'date':date,
            'time':time
          }
        }
        context.commit("set_movie", data.movie);
        context.commit("set_movie_sessions", data.movie_sessions);
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
    set_movie_sessions(state, movie_s) {
      state.movie_sessions = movie_s;
    },
  },
  state: {
    movies: [],
    movie: null,
    movie_sessions: [],
  },
  getters: {
    allMovies(state) {
      return state.movies;
    },
    currentMovie(state) {
      return state.movie;
    },
    movieSessions(state) {
      console.log(state.movie_sessions);
      return state.movie_sessions;
    },
  },
};

export default movieModule;
