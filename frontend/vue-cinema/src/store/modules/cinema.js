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
      CinemaService.getCinema(pk).then((cinema) => {
        context.commit("set_cinema", cinema);
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
  },
  state: {
    cinemas: [],
    cinema: null,
  },
  getters: {
    allCinemas(state) {
      return state.cinemas;
    },
    currentCinema(state) {
      return state.cinema;
    },
  },
};

export default cinemaModule;
