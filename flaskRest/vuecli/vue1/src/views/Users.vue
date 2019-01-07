<template>
  <div>
    <UserTable/>
  </div>
</template>
<script>
import UserTable from "@/components/UserTable.vue";
export default {
  name: "users",
  components: { UserTable }
};
</script>