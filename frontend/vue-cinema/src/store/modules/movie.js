import MovieService from "../../services/MovieService";


const movieModule = {
  actions: {
    getMovies(context) {
      MovieService.getMovies().then((movies) => {
        console.log(movies)
        context.commit("set_movies", movies);
      });
    },
    getMoviesSoon(context) {
      MovieService.getMoviesSoon().then((movies) => {
        console.log("movies soon", movies);

        context.commit("set_movies_soon", movies);
      });
    },
    getLatestMovies(context) {
      MovieService.getMoviesLatest().then((movies) => {
        console.log("latest movies", movies);
        context.commit("set_latest_movies", movies);
      });
    },
     getMovie(context, pk) {
      MovieService.getMovie(pk).then((data) => {
        console.log("only movie", data.movie);
        console.log("only ms", data.movie_sessions);

        for (var ms_key in data.movie_sessions) {
          let movie_sessions = data.movie_sessions[ms_key];
          let new_date = new Date(movie_sessions["datetime_session"]);
          var date = new_date.toLocaleDateString("ru", {
            weekday: "long",
            year: "numeric",
            month: "long",
            day: "numeric",
          });
          var time = new_date.toLocaleTimeString("ru");
          movie_sessions["datetime_session"] = {
            date: date,
            time: time,
          };
        }
        context.commit("set_movie", data.movie);
        context.commit("set_movie_sessions", data.movie_sessions);
      });
    },
    getFilterMovies(context, filters) {
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
    set_latest_movies(state, latest_movies) {
      state.latest_movies = latest_movies;
    },
    set_movies_soon(state, movies_soon) {
      state.movies_soon = movies_soon;
    },
  },
  state: {
    movies: [],
    movie: null,
    movie_sessions: [],
    latest_movies: [],
    movies_soon: [],
  },
  getters: {
    allMovies(state) {
      return state.movies;
    },
    movieSoon(state) {
      return state.movies_soon;
    },
    latestMovie(state) {
      return state.latest_movies;
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
