import { HTTP_USER } from "../http-common.js";
import HTTP from "../http-common.js";



// const showPDF = (function () {
//   return function (blob, fileName) {
//     var newBlob = new Blob([blob], {type: 'application/pdf'})
//     if (window.navigator && window.navigator.msSaveOrOpenBlob) {
//     window.navigator.msSaveOrOpenBlob(newBlob)
//     return
//     }
//     const data = window.URL.createObjectURL(newBlob)
//     var link = document.createElement('a')
//     link.href = data
//     link.click()
//     window.open(data)
//     setTimeout(function () {
//       document.body.removeChild(link)
//       window.URL.revokeObjectURL(data)
//       100
//       })
//    }
// }())

const UserProfileService = {
  getUserReport() {
    return HTTP_USER.get(`/profile/report/`).then((response) => {
      console.log(response.data);
      return response.data;
    });
  },
  downloadTickets() {
    return HTTP_USER.get(`/profile/download-booked-tickets//`).then(
      (response) => {
        console.log(response.data);
        return response.data;
      }
    );
  },
  getUserBookedTickets(ids_booked) {
    console.log(ids_booked);

    // change url
    return HTTP_USER.post(`/profile/booked-tickets/`, {
      booked_ids: ids_booked,
    }).then((response) => {
      console.log(response.data);
      var data = response.data;
      for (var i in data) {
        let bookings = data[i];
        console.log(data, bookings);
        console.log(bookings["session"]);

        let session = bookings["session"];
        console.log(session);

        let new_date = new Date(session["datetime_session"]);
        session["datetime_session"] = new_date.toLocaleString();
      }
      return response.data;
    });
  },
  deleteUserBooking(pk) {
    console.log("delete booking ");
    return HTTP.delete(`/booking/${pk}/`)
      .then((response) => {
        console.log(response.data);
        return response.data;
      })
      .catch((error) => {
        throw error;
        this.errorMessage = error.message;
        console.error("There was an error!", error);
        return error;
      });
  },
};
export default UserProfileService;
