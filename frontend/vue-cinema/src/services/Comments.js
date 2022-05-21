import HTTP from "../http-common";

const CommentsService = {
  getComments(pk) {
    return HTTP.get(`/movie/${pk}/comments/`).then((response) => {
      console.log('here',response.data);
      let comments = response.data;
      
      for (var i in comments) {
        let comment = comments[i]
        let new_date = new Date(comment["date"]);
        comment["date"] = new_date.toLocaleString();
        // var date = new_date.toLocaleDateString("en", {
        //   weekday: "long",
        //   year: "numeric",
        //   month: "long",
        //   day: "numeric",
        // });
        // var time = new_date.toLocaleTimeString("en-US");
        // comment["date"] = {
        //   date: date,
        //   time: time,
        // };
      }
      return comments;
    });
  },
  postComment(data) {
    console.log(data);
    return HTTP.post(
        `/comment/`, data
      ).then((response) => {
          data = response.data
          console.log(data)
        return data;
      }).catch(error => {
        throw error;
        this.errorMessage = error.message;
        console.error("There was an error!", error);
        return error;
      });
  },
};
export default CommentsService;
