<template>
  <div class="d-flex align-start flex-column ml-5">
    <FriendsCard
      v-for="item of items"
      :key="item._id"
      :id="item._id"
      :firstName="item.name.first"
      :lastName="item.name.last"
      :email="item.email"
      :picture="item.picture"
      :lat="item.location.latitude"
      :lon="item.location.longitude"
    >
      <!--        <div @click="onClick">{{ item.name.first }} {{ item.name.last }}</div>-->
    </FriendsCard>
  </div>
</template>

<script setup>
import FriendsCard from "../components/FriendsCard.vue";
</script>

<script>
import axios from "axios";

const config = {
  headers: { Authorization: `Bearer v3srs6i1veetv3b2dolta9shrmttl72vnfzm220z` },
};
export default {
  name: "FriendsList",
  data() {
    return {
      items: [],
    };
  },
  async created() {
    try {
      const res = await axios.get(
        "https://api.json-generator.com/templates/-xdNcNKYtTFG/data",
        config
      );
      this.items = res.data;
    } catch (error) {
      console.log(error);
    }
  },
  methods: {
    onClick() {
      console.log("clicked");
    },
  },
};
</script>

<style scoped></style>
