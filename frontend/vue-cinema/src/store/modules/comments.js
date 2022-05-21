import CommentsService from "../../services/Comments.js";

const commentsModule = {
  actions: {
    async getComments(context, pk) {
      CommentsService.getComments(pk).then((data) => {
        console.log("from get comments module");

        context.commit("set_comments", data);
      });
    },
    async postComment(context, data) {
        CommentsService.postComment(data).then((data) => {
          console.log("from post comments module", data);
          context.commit("set_new_comment", data);
        });
      },
  },
  mutations: {
    set_comments(state, comments) {
      state.comments = comments;
    },
    set_new_comment(state, new_comment) {
      state.new_comment = new_comment;
    },
  },
  state: {
    allComments: [],
    newComment: null,
  },
  getters: {
    allComments(state) {
      return state.comments;
    },
    newComment(state) {
      return state.new_comment;
    },
  },
};

export default commentsModule;
