// import CinemaService from "./services/DataService";
import UserProfileService from "../../services/UserProfile";

const profileModule = {
  actions: {
    async getUserReport(context) {
      UserProfileService.getUserReport().then((data) => {
        console.log("REPORT ", data);
        for (var i in data) {
          let bookings = data[i];
          for (var j in bookings) {
            let booking = bookings[j];
            let session = booking["session"];
            let new_date = new Date(session["datetime_session"]);
            session["datetime_session"] = new_date.toLocaleString();
          }
        }
        context.commit("set_history_booking", data["booked_seat"]);
        context.commit("set_current_booking", data["current_booked"]);
      });
    },
    async deleteBooking(context, pk) {
      UserProfileService.deleteUserBooking(pk).then((report) => {
        console.log("delete booking  ", pk);
      });
    },
  },
  mutations: {
    set_current_booking(state, current_booking) {
      state.current_booking = current_booking;
    },
    set_history_booking(state, history_booking) {
      state.history_booking = history_booking;
    },
  },
  state: {
    current_booking: [],
    history_booking: [],
    delete_booking: [],
  },
  getters: {
    currentBooking(state) {
      return state.current_booking;
    },
    historyBooking(state) {
      return state.history_booking;
    },
  },
};

export default profileModule;
