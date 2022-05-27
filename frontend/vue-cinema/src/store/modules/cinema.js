// import CinemaService from "./services/DataService";
import CinemaService from "../../services/CinemaService.js";

const cinemaModule = {
  actions: {
    async getCinemas(context) {
      CinemaService.getCinemas().then((cinemas) => {
        context.commit("set_cinemas", cinemas);
      });
    },
    async getCinema(context, pk) {
      CinemaService.getCinema(pk).then((data) => {
        console.log(data.cinema, data.movie_session)

        for (var ms_key in data.movie_sessions) {
          console.log(ms_key, data.movie_sessions[ms_key])
          let movie_sessions = data.movie_sessions[ms_key];
          let new_date = new Date(movie_sessions["datetime_session"]);
          var date = new_date.toLocaleDateString('en', { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' })
          var time = new_date.toLocaleTimeString('en-US')
          movie_sessions["datetime_session"] = {
            'date':date,
            'time':time
          }
        }


        context.commit("set_cinema", data.cinema);
        context.commit("set_movie_session", data.movie_session);

        context.commit("set_cinema_ms", data.movie_session);
      });
    },
  },
  mutations: {
    set_cinemas(state, cinemas) {
      state.cinemas = cinemas;
    },
    set_cinema(state, cinema) {
      state.cinema = cinema;
    },
    set_cinema_ms(state, cinema_ms) {
      state.cinema_ms = cinema_ms;
    },
  },
  state: {
    cinemas: [],
    cinema: null,
    cinema_ms:[]
  },
  getters: {
    allCinemas(state) {
      return state.cinemas;
    },
    currentCinema(state) {
      return state.cinema;
    },
    cinemaSessions(state) {
      return state.cinema_ms;
    },
  },
};

export default cinemaModule;
