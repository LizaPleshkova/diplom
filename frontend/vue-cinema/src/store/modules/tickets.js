// import CinemaService from "./services/DataService";
import UserProfileService from "../../services/UserProfile";

const ticketsModule = {
  actions: {
    async getUserBookedTickets(context, ids) {
      UserProfileService.getUserBookedTickets(ids).then((data) => {
        // CHANGE

        console.log("TICKETs ", data);
        // for (var i in data) {
        //   let bookings = data[i];
        //   for (var j in bookings) {
        //     let booking = bookings[j];
        //     let session = booking["session"];
        //     let new_date = new Date(session["datetime_session"]);
        //     session["datetime_session"] = new_date.toLocaleString();
        //   }
        // }
        context.commit("set_bookings", data);
      });
    },
    async downloadTickets(context) {
      UserProfileService.downloadTickets().then((data) => {
        // CHANGE

        console.log("TICKETs file", data);

        context.commit("set_tickets_file", data);
      });
    },
  },
  mutations: {
    set_bookings(state, current_bookings) {
      state.bookings = current_bookings;
    },
    set_tickets_file(state, file) {
      state.tickets_file = file;
    },
  },
  state: {
    tickets_file: [],
    bookings: [],
  },
  getters: {
    ticketsFile(state) {
      return state.tickets_file;
    },
    Bookings(state) {
      return state.bookings;
    },
  },
};

export default ticketsModule;
