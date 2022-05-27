import { HTTP_USER } from "../http-common.js";
import HTTP from "../http-common.js";

const UserProfileService = {
  getUserReport() {
    return HTTP_USER.get(`/profile/report/`).then((response) => {
      console.log(response.data);
      return response.data;
    });
  },
  deleteUserBooking(pk) {
    console.log('delete booking ');
    return HTTP.delete(`/booking/${pk}/`).then((response) => {
      console.log(response.data);
      return response.data;
    }).catch(error => {
      throw error;
      this.errorMessage = error.message;
      console.error("There was an error!", error);
      return error;
    });
  },
};
export default UserProfileService;
