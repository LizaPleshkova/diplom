<template>
  <div class="card mx-auto left-ads-display col-lg-12">
    <div class="container mt-5">
      <div class="row d-flex justify-content-center">
        <div class="col-md-7">
          <div class="shadow p-3 bg-white rounded">
            <div class="d-flex justify-content-between align-items-center">
              <div class="d-flex flex-row align-items-center">
                <select class="sort_by" v-model="sortedBy">
                  <option selected disabled>SORT BY</option>
                  <option value="newest"> Sort By Newest</option>
                  <option value="oldest">Sort By Oldest</option>
                </select>
                {{ sortedBy }}
                <div class="col-sm-12 m-1 text-center " v-if='errorMessage'>
                  <div class="alert alert-warning" role="alert">
                    {{ errorMessage }}
                  </div>
                </div>
                <div class="col-sm-12 m-1 text-center " v-if='newComment.length != 0'>
                  <div class="alert alert-success" role="alert">
                    <h6> Спасибо за ваш комментарий! Сейчас он находится на обработке модератором.</h6>
                  </div>
                </div>
              </div>
            </div>
            <div class="mt-5 d-flex flex-row">
              <img src="https://i.imgur.com/jD4jCW9.png" width="40" height="40" />
              <div class="w-100 ml-2 comment-area">
                <textarea class="form-control" v-model="comment.text"></textarea>
                <button class="btn btn-secondary btn-block mt-2 post-btn" value="submit" v-on:click="postNewComment">
                  Post
                </button>
              </div>
            </div>
            <div v-for="comment in allComments" :key="comment.id" class="d-flex flex-row mt-4">
              <img src="https://i.imgur.com/jD4jCW9.png" width="40" height="40" />
              <div class="ml-2 w-100">
                <div class="d-flex justify-content-between align-items-center">
                  <div class="d-flex flex-row align-items-center">
                    <span class="font-weight-bold name">{{ comment.author.username }} <i class="fa fa-heart"></i></span>
                    <span class="dots"></span>
                    <small class="text-muted time-text"> {{ comment.date }}</small>
                  </div>
                  <span class="top-comment">Top comment <i class="fa fa-star"></i></span>
                </div>
                <p class="user-comment-text text-justify">{{ comment.text }}</p>
                <div class="mt-3 d-flex align-items-center">
                  <!-- <span class="fs-13">Reply</span> <span class="dots"></span> -->
                  <span class="fs-13">100 likes</span>
                  <!-- <span class="dots"></span> -->
                  <span>
                    <i class="fa fa-thumbs-up"></i>
                    <i class="fa fa-thumbs-down"></i>
                  </span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import CommentsService from "@/services/Comments.js";

export default {
  name: "CommentsMovie",
  data() {
    return {
      sortedBy: "newest",
      nullStr: " ",
      comment: {
        text: "",
        movie: "",
      },
      errorMessage: null,
      // allComments: [],
      newComment: [],

    };
  },
  computed: mapGetters(["allComments"]),
  watch: {
    sortedBy(newSort, oldSort) {
      if (newSort !== oldSort) {
        this.sortComments();
      }
    },
    newComment(n_newComment, o_newComment) {
      if (n_newComment !== o_newComment) {
        this.getComments(this.$route.params.movieId);
      }
    }
  },
  methods: {
    ...mapActions(["getComments", "postComment"]),
    postNewComment: async function () {
      this.comment.movie = this.$route.params.movieId;
      console.log(this.comment);
      // this.$store.dispatch("postComment", this.comment);
      CommentsService.postComment(this.comment).then((data) => {
        console.log("from post comments module", data);
        this.newComment = data;
      }).catch(error => {
        this.errorMessage = error.message;
        console.error("There was an error!", error);
        return error;
      });
      console.log('newComment', this.newComment);
      // this.$store.dispatch.getComments(this.$route.params.movieId);
    },
    sortComments() {
      console.log(this.allComments)
      // a.reverse()
      // this.allComments.sort(SortArray);
      switch (this.sortedBy) {
        case "oldest":
          // this.allComments.sort(SortArray);
          this.allComments.sort((a, b) => {
            if (a.date < b.date)
              return -1;
            if (a.date > b.date)
              return 1;
            return 0;
          });
          break;
        case "newest":
          // this.allComments.sort(SortArray).reverse();
          this.allComments.sort((a, b) => {
            if (a.date < b.date)
              return -1;
            if (a.date > b.date)
              return 1;
            return 0;
          }).reverse();
          break;
      }
      console.log("omments sort", this.allComments);
    },
  },
  created() {
    this.getComments(this.$route.params.movieId);
  },
};
</script>
