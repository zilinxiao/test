<template>
  <div class="home">
    <!-- <img alt="Vue logo" src="../assets/logo.png"> -->
    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
    <UserOperate/>
    <br>
    <UserTable />
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'
import UserTable from "@/components/UserTable.vue";
import UserOperate from "@/components/UserOperate.vue";

export default {
  name: "home",
  components: {
    // HelloWorld
    UserTable,
    UserOperate
  }
}
</script>
