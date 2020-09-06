<template>
  <div class="dashboard-container">
    <!-- <div class="dashboard-text">name: {{ name }}</div> -->
    <el-row>
    <el-col :span="24"> <img src="../../assets/user_log.jpg" class="profile_photo"/> </el-col>
    </el-row>

    <el-row>
    <el-col :span="24"> <h1 align="center" padding-top="20px" style="font-family: 'jdjszhong'; font-weight: bold; display:block;"> {{ name }}
    <img src="../../assets/stu.png" class="icon" title="学生认证">  </h1>  </el-col>
    </el-row>

    <el-row>
    <el-col :span="24"> <p align="center" class="discription" style="font-family: 'jdjszhong'; font-weight: bold; display:block;"> 个人简介：{{ description }} </p> </el-col>
    </el-row>

    <el-row>
    <el-col :span="12"> <h1 class="one" style="font-family: 'jdjszhong'; font-weight: bold; display:block;"> 年龄：{{ age }} </h1> </el-col>
    <el-col :span="12"> <h1 class="two" style="font-family: 'jdjszhong'; font-weight: bold; display:block;"> 信用分：{{ credit }} </h1> </el-col>
    </el-row>

    <div
      v-for="activity in history_activity"
      :key="activity.title"
      class='box row' style="font-family: 'jdjszhong'; font-weight: bold; display:block;">
        <div>
          <el-row>
            <el-col :span="4"> <p class="title"> {{ activity.title }} </p> </el-col>
            <el-col :span="16"> <p> {{ activity.description }} </p> </el-col>
            <el-col :span="4">
              <div class="four">
                <el-tag :type="activity.status | statusFilter" class="three">{{ activity.status }}</el-tag>
              </div>
            </el-col>
          </el-row>

        </div>
    </div>

  </div>
</template>

<script>
// import { mapGetters } from 'vuex'

export default {
  name: 'Dashboard',
  filters: {
    statusFilter(status) {
      const statusMap = {
        finished: 'success',
        in_progress: 'gray',
        cancel: 'danger'
      }
      return statusMap[status]
    }
  },
  data() {
    return {
      name: '深小爱',
      age: 23,
      credit: 687,
      description: '我在深圳等你找我玩',
      history_activity: [
        {title: '香港中文大学（深圳）', description: 'FREE', status: 'in_progress'},
        {title: '欢乐时光', description: '90% OFF', status: 'cancel'},
        {title: '月石剧本杀', description:'90% OFF', status: 'finished'}
      ]
    }
  },
  mounted() {
    // this.getData()
  },
  methods: {
    getData() {
      this.axios
        .post('/hello_api', {
          input: 'nihao'
        })
        .then((res) => {
          this.name = res.data['hello']
        })
        .catch((error) => {
          alert(error)
        })
    }
  }
}
</script>

<style lang="scss" scoped>
.four {
  position: absolute;
  right: 10%;
  top: 20%;
  text-align: center;
  font-size: 16px;
}
.three {
  //width: 5%;
  position: relative;
  font-size: 16px;
  top: 100%;
}
.one {
  position: absolute;
  left: 30%;
}
.two {
  position: relative;
  left: 120%;
}
.dashboard {
  &-container {
    margin-left: 40px;
    margin-right: 40px;
    // margin-top: 20px;
    // border-style:solid;
    background: url('../../assets/bgpic.png');
    background-repeat : none;
    background-size: cover;
  }
  &-text {
    font-size: 30px;
    line-height: 46px;
  }
}

.profile_photo{
  position: relative;
  width: 200px;
  //margin-left: 580px;
  margin-top: 20px;
  left: 40%;
  border-radius:100px;
  border: 1;
  border-style: solid;
}
.box{
  // border-radius: 10%;
  box-shadow: 0px 0px 5px #a094b7;
  background-color: white;
  box-sizing: border-box;
  padding: 20px;
  margin: 20px;
}
.box{
  .title{
    font-weight:bold;
  }
}
.icon{
  width: 30px;
}
.discription{
  font-size: 21px;
  box-shadow: 0px 0px 5px #a094b7;
  background-color: white;
  box-sizing: border-box;
  padding: 20px;
  margin: 20px 250px;
  height: 120px;
}
</style>
