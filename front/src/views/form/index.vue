<template>
  <div class="app-container" style="font-family: 'Blacker Text'; font-weight: bold; display:block;">
    <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="120px" class="demo-ruleForm">
      <el-form-item label="Activity name" prop="name">
        <el-input v-model="ruleForm.name"></el-input>
      </el-form-item>
      <el-form-item label="Member" prop="name" style="width: 30%">
        <el-input v-model="ruleForm.number"></el-input>
      </el-form-item>
      <el-form-item label="Activity time" required>
        <el-col :span="11">
          <el-form-item prop="date1">
            <el-date-picker type="date" placeholder="Pick a date" v-model="ruleForm.date1" style="width: 100%;"></el-date-picker>
          </el-form-item>
        </el-col>
        <el-col class="line" :span="2">-</el-col>
        <el-col :span="11">
          <el-form-item prop="date2">
            <el-time-picker placeholder="Pick a time" v-model="ruleForm.date2" style="width: 100%;"></el-time-picker>
          </el-form-item>
        </el-col>
      </el-form-item>

      <el-form-item label="Randomness" prop="randomness" class="random" inline="true">
        <el-switch v-model="ruleForm.randomness"></el-switch>
      </el-form-item>
      <el-form-item label="Resources" prop="resource">
        <el-radio-group v-model="ruleForm.resource">
          <el-radio label="Enterprise"></el-radio>
          <el-radio label="Individual"></el-radio>
        </el-radio-group>
      </el-form-item>
      <el-form-item label="Position" prop="position">
        <el-input v-model="ruleForm.position"></el-input>
      </el-form-item>
      <el-form-item label="Activity form" prop="desc" inline="true">
        <el-input type="textarea" v-model="ruleForm.desc"></el-input>
      </el-form-item>
      <el-form-item class="btn2">
        <el-button type="primary" @click="submitForm('ruleForm')" class="btn" style="font-family: 'Blacker Text'; font-weight: bold;">Create</el-button>
        <el-button @click="resetForm('ruleForm')" style="font-family: 'Blacker Text'; font-weight: bold;">Reset</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
export default {
    data() {
      return {
        ruleForm: {
          name: '',
          number: '',
          date1: '',
          date2: '',
          randomness: false,
          type: [],
          resource: '',
          desc: ''
        },
        rules: {
          name: [
            { required: true, message: 'Please input Activity name', trigger: 'blur' },
          ],
          number: [
            { required: true, message: 'Please input a member number', trigger: 'blur' },
          ],
          date1: [
            { type: 'date', required: true, message: 'Please pick a date', trigger: 'change' }
          ],
          date2: [
            { type: 'date', required: true, message: 'Please pick a time', trigger: 'change' }
          ],
          type: [
            { type: 'array', required: true, message: 'Please select at least one activity type', trigger: 'change' }
          ],
          resource: [
            { required: true, message: 'Please select activity resource', trigger: 'change' }
          ],
          randomness:[
            { required: true, message: 'Please select random or not'}
          ],
          desc: [
            { required: true, message: 'Please input activity description', trigger: 'blur' }
          ],
          position: [
            { required: true, message: 'Please input position', trigger: 'blur' }
          ],
        }
      };
    },
    methods: {
    submitForm(formName) {
        // this.$refs[formName].validate((valid) => {
        //   if (valid) {
        //     console.log(this.ruleForm)
        //     this.$axios({
        //       url: '/zs/zhgl/handleSubmitZh',
        //       method: 'post',
        //       data: this.ruleForm
        //     }).then(ref => {
        //       if (ref.result) {
        //         this.$message({
        //           message: this.$t('zsgl_zhgl.xxbccg'),
        //           type: 'success'
        //         })
        //       } else {
        //         this.$message.error(ref.msg)
        //       }
        //
        //     this.$message({
        //       message: 'Submit Sucessful!',
        //       type:'success'
        //     });
        //   } else {
        //     console.log('error submit!!');
        //     return false;
        //   }
        // });
      },
      resetForm(formName) {
        this.$refs[formName].resetFields();
      }
    },
}
</script>

<style scoped>
.line{
  text-align: center;
}
.btn{
  background-color: #274c4a;
}
.btn2{
  margin-top: 55px;
  left: 270px;
  position: relative;
}
</style>


