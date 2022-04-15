// import CinemaService from "./services/DataService";
import FilterService from "../../services/FilterService.js";

const filterModule = {
  actions: {
    async getFilters(context) {
        FilterService.getFilters().then((filters) => {
          console.log('',filters["cinemas"]);
        context.commit("set_cinemas", filters["cinemas"]);
        context.commit("set_genres",  filters["dates"]);
        context.commit("set_dates", filters["genres"]);
      });
    }
  },
  mutations: {
    set_cinemas(state, cinemas) {
      state.cinemas = cinemas;
    },
    set_genres(state, genres) {
      state.genres = genres;
    },
    set_dates(state, dates) {
      state.dates = dates;
    },
  },
  state: {
    cinemas: [],
    genres:[],
    dates:[],
  },
  getters: {
    f_cinemas(state) {
      return state.cinemas;
    },
    f_genres(state) {
      return state.genres;
    },
    f_dates(state) {
      return state.dates;
    },
    
  },
};

export default cinemaModule;
