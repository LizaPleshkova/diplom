<template>
    <div>
        <div class="col-sm-12 text-left">
            <div class="container hero-gray-card d-flex align-items-center">
                <div class="container ground-opacity">
                    <div class="col">
                        <div class="row d-flex justify-content-center">
                            <h1>Актуальные забронированные места</h1>
                        </div>
                        <br>
                        <div class="col-sm-12 m-1 text-center " v-if='errorMessage'>
                            <div class="alert alert-warning" role="alert">
                                {{ errorMessage }}
                            </div>
                        </div>

                        <p>
                            Эти данные можно скачать в формате pdf. Для этого нажмите
                            <router-link :to="{ name: 'user-tickets', params: { selectedBookingIds: selectedBooking } }"
                                class="btn btn-outline-success btn-sm"> Просмотреть электронные билеты
                            </router-link>
                        </p>


                        <div class="row d-flex justify-content-center" v-if='currentBooking.length != 0'>
                            <table class="table">
                                <thead>
                                    <tr>
                                        <th scope="col">#</th>
                                        <th scope="col">Кинотеатр</th>
                                        <th scope="col">Киносеанс</th>
                                        <th scope="col">Место</th>
                                        <th scope="col">Цена</th>
                                        <th scope="col">Дата бронирования</th>
                                        <th scope="col">Снять бронирование</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <th scope="row"></th>
                                    <tr v-for="(booked, ind) in currentBooking" :key="booked.id">
                                       <td> <label class="check text-center">
                                            <!-- {{ ind }} -->
                                            <input type="checkbox" :id="ind" :value="booked.id"
                                                v-model="selectedBooking" />
                                            <span class="checkmark" :for="ind"></span>
                                        </label>
                                        </td>
                                        <td>  Кинотеатр {{ booked.cinema.name }}, {{ booked.cinema.address }}
</td>
                                        <td>Фильм {{ booked.session.movie }}, Зал {{ booked.session.hall }},
                                        {{ booked.session.datetime_session}}
                                        </td>
                                        <td>{{ booked.seat.number_place }} место, {{ booked.seat.number_row }} ряд,
                                            сектор {{ booked.seat.sector }}
                                        </td>
                                        <td>{{ booked.price }}</td>
                                        <td>{{ booked.datetime_book }}</td>
                                        <td class="d-flex justify-content-center">
                                            <button type="submit" class="btn btn-outline-danger"
                                                v-on:click="deleteBooking(booked.id)">удалить</button>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>

                        </div>
                        <h5 v-else>На данный момент у вас нет заброннированных мест</h5>
                    </div>
                </div>
            </div>
        </div>

       <div class="col-sm-12 text-left">
            <div class="container hero-gray-card d-flex align-items-center">
                <div class="container ground-opacity">
                    <div class="col">
                        <div class="row d-flex justify-content-center">
                            <h1>История забронированных мест</h1>
                        </div>
                        <br>
                        <div class="row d-flex justify-content-center" v-if='historyBooking.length != 0'>
                            <!-- <p>
                                Эти данные можно скачать в формате pdf. Для этого нажмите
                                <router-link
                                    :to="{ name: 'user-tickets', params: { selectedBooking: selectedBooking } }"
                                    class="btn btn-outline-success btn-sm">Downland PDF
                                </router-link>
                            </p> -->

                            <div class="row d-flex justify-content-center">
                                <table class="table align-items-center">
                                    <thead>
                                        <tr>
                                            <th scope="col">#</th>
                                            <th scope="col">Киносеанс</th>
                                            <th scope="col">Место</th>
                                            <th scope="col">Цена</th>
                                            <th scope="col">Дата брони</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr v-for="(booked, ind) in historyBooking" :key="booked.id"
                                            class="justify-content-center align-items-center">

                                            <!-- <th scope="row"></th> -->
                                            <td>{{ ind }}
                                            </td>
                                            <td>{{ booked.session.movie }}, {{ booked.session.hall }},
                                                {{ booked.session.datetime_session }}
                                            </td>
                                            <td> место {{ booked.seat.number_place }}, {{ booked.seat.number_row }} ряд,
                                                сектор {{ booked.seat.sector }}
                                            </td>
                                            <td>{{ booked.price }}</td>
                                            <td>{{ booked.datetime_book }}
                                            </td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                        </div>
                        <h5 v-else>На данный момент у вас нет истории заброннрованных мест</h5>

                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import UserProfileService from "@/services/UserProfile";

export default {
    name: "Profile",
    data() {

        // ADD CHECKBOXES IN FIRST COLUMNS EACH ROW
        return {
            selectedBooking: [],
            errorMessage: null,
            idsDeleteBooking: "id" + Math.random().toString(16).slice(2),
        }
    },
    computed: mapGetters(["currentBooking", "historyBooking"]),
    watch: {
        idsDeleteBooking(newIdBooking, oldIdBooking) {
            if (newIdBooking !== oldIdBooking) {
                this.getUserReport();
            }
        }
    },
    methods: {
        ...mapActions(["getUserReport", "deleteBooking"]),
        deleteBooking(pk) {
            console.log(this.newComment);
            console.log("del in profile vue", pk);
            // this.$store.dispatch("deleteBooking", pk);
            UserProfileService.deleteUserBooking(pk).then((report) => {
                console.log("delete booking  ", pk);
                this.idsDeleteBooking = pk.toString() + Math.random().toString(16).slice(2);
                // this.getUserReport(context);
            }).catch(error => {
                this.errorMessage = error.message;
                console.error("There was an error!", error);
                return error;
            });
            console.log("currentBooking")
            const newData = this.currentBooking.filter(item => { console.log(item.id); item.id !== pk; })


            console.log(newData, this.currentBooking)
            this.currentBooking = newData;
            //   this.getUserReport();
        }
    },
    created() {
        console.log("currentBooking", this.currentBooking)
        this.getUserReport();
    },
    mounted() {
        console.log("currentBooking", this.currentBooking)
        this.getUserReport();
    },
};
</script>

<style>
/* The radio */
.radio {
    display: block;
    position: relative;
    padding-left: 30px;
    margin-bottom: 12px;
    cursor: pointer;
    font-size: 10px;
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
}

/* Hide the browser's default radio button */
.radio input {
    position: absolute;
    opacity: 0;
    cursor: pointer;
}

/* Create a custom radio button */
.checkround {
    position: absolute;
    top: 6px;
    left: 0;
    height: 20px;
    width: 20px;
    background-color: #fff;
    border-color: #13c931;
    border-style: solid;
    border-width: 2px;
    border-radius: 50%;
}

/* When the radio button is checked, add a blue background */
.radio input:checked~.checkround {
    background-color: #fff;
}

/* Create the indicator (the dot/circle - hidden when not checked) */
.checkround:after {
    content: "";
    position: absolute;
    display: none;
}

/* Show the indicator (dot/circle) when checked */
.radio input:checked~.checkround:after {
    display: block;
}

/* Style the indicator (dot/circle) */
.radio .checkround:after {
    left: 2px;
    top: 2px;
    width: 12px;
    height: 12px;
    border-radius: 50%;
    background: #09b425;
}

/* The check */
.check {
    /* justify-content-around; */
    display: block;
    position: relative;
    padding-left: 25px;
    margin-bottom: 12px;
    padding-right: 15px;
    cursor: pointer;
    font-size: 15px;
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
}

/* Hide the browser's default checkbox */
.check input {
    position: absolute;
    opacity: 0;
    cursor: pointer;
}

/* Create a custom checkbox */
.checkmark {
    position: absolute;
    top: 3px;
    left: 0;
    height: 18px;
    width: 18px;
    background-color: #fff;
    border-color: #08c904;
    border-style: solid;
    border-width: 2px;
}

/* When the checkbox is checked, add a blue background */
.check input:checked~.checkmark {
    background-color: #fff;
}

/* Create the checkmark/indicator (hidden when not checked) */
.checkmark:after {
    content: "";
    position: absolute;
    display: none;
}

/* Show the checkmark when checked */
.check input:checked~.checkmark:after {
    display: block;
}

/* Style the checkmark/indicator */
.check .checkmark:after {
    left: 5px;
    top: 1px;
    width: 5px;
    height: 10px;
    border: solid;
    border-color: #f8204f;
    border-width: 0 3px 3px 0;
    -webkit-transform: rotate(45deg);
    -ms-transform: rotate(45deg);
    transform: rotate(45deg);
}

.cust-btn {
    margin-bottom: 10px;
    background-color: #f8204f;
    border-width: 2px;
    border-color: #f8204f;
    color: #fff;
}

.cust-btn:hover {
    border-color: #f8204f;
    background-color: #fff;
    color: #f8204f;
    border-radius: 20px;
    transform-style: 2s;
}
</style>