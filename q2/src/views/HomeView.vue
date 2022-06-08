<script setup>
// import TheWelcome from "@/components/TheWelcome.vue";
import FriendsList from "../components/FriendsList.vue";
</script>

<template>
  <main>
    <v-container class="grey lighten-5">
      <v-row>
        <v-col sm="6">
          <v-toolbar>
            <v-app-bar-title>
              Friend List
            </v-app-bar-title>
          </v-toolbar>
          <FriendsList />
        </v-col>
      </v-row>
    </v-container>
  </main>
</template>
