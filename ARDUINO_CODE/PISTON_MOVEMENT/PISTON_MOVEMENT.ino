#define strt_btn 3
int pstn[3][2] = {{8,9},{10,11},{12,13}};
int pstn_len[3], steps = 0, nmnl_ht = 100, tilt_ht = 20, angle, steps_to_move;
int crrnt_pstn_ht[3];

///////////////////////////////////////////////////////////////move_down/////////////////////////////////////////////////////////////
void move_dwn(int pstn_num,int delay_time){
  digitalWrite(pstn[pstn_num][0],LOW);
  digitalWrite(pstn[pstn_num][1],HIGH);
  delay(delay_time);
  digitalWrite(pstn[pstn_num][1],LOW);
}

///////////////////////////////////////////////////////////////move_up/////////////////////////////////////////////////////////////
void move_up(int pstn_num,int delay_time){
  digitalWrite(pstn[pstn_num][0],HIGH);
  digitalWrite(pstn[pstn_num][1],LOW);
  delay(delay_time);
  digitalWrite(pstn[pstn_num][0],LOW);
}

///////////////////////////////////////////////////////////////change piston height//////////////////////////////////////////////////
void set_pstn_ht(int pstn_num, int pstn_ht){
  
  steps_to_move = pstn_ht - crrnt_pstn_ht[pstn_num];
  if(steps_to_move < 0){
    steps_to_move = 0 - steps_to_move;
    move_dwn(pstn_num,steps_to_move);
  }else move_up(pstn_num,steps_to_move);
  crrnt_pstn_ht[pstn_num] = pstn_ht;
  
}

//////////////////////////////////////////////////////////////////////void setup///////////////////////////////////////////
void setup() {

  Serial.begin(9600);
  
  for(int i=0;i<3;i++){
    for(int j=0;j<2;j++){
      pinMode(pstn[i][j],OUTPUT);
      //Serial.println(pstn[i][j]);
    }
  }

  Serial.println("Intialising...");

  long start_time = millis();
  long end_time = start_time;
  while ((end_time - start_time) <= 20000) // do this loop for up to 20s
  {
    for(int i=0;i<3;i++){
      move_dwn(i,500);
    }
    end_time = millis();
  }

  Serial.println("Done!");
  Serial.println("Press START");

  while(1){
    if(digitalRead(strt_btn)){
      while(steps <= nmnl_ht){
        for(int i=0;i<3;i++){
          move_up(i,500);
          steps++;
        }  
      }
      crrnt_pstn_ht[0] = nmnl_ht;
      crrnt_pstn_ht[1] = nmnl_ht;
      crrnt_pstn_ht[2] = nmnl_ht;
      break;
    }
  }

}

/////////////////////////////////////////////////////////////////void loop/////////////////////////////////////////////////////
void loop() {
  
  //angle = get_angle();
  get_pstn_len(angle);
  for(int i = 0; i < 3; i++){
    set_pstn_ht(i,pstn_len[i]);
  }
  long start_time = millis();
  long end_time = start_time;
  int minutes_elapsed;
  while (minutes_elapsed <= 5) // do this loop for up to 20s
  {
    delay(60000);
    minutes_elapsed++;
  }
  for(int i = 0; i < 3; i++){
    set_pstn_ht(i,nmnl_ht);
  }
  
}

///////////////////////////////////////////////////////////////get piston length//////////////////////////////////////////////////
void get_pstn_len(int angle){
  switch(angle){
    case 0:
      pstn_len[0] = nmnl_ht + tilt_ht;
      pstn_len[1] = nmnl_ht - tilt_ht;
      pstn_len[2] = nmnl_ht - tilt_ht;
      break;
    case 60:
      pstn_len[0] = nmnl_ht + tilt_ht;
      pstn_len[1] = nmnl_ht - tilt_ht;
      pstn_len[2] = nmnl_ht + tilt_ht;
      break;
    case 120:
      pstn_len[0] = nmnl_ht - tilt_ht;
      pstn_len[1] = nmnl_ht - tilt_ht;
      pstn_len[2] = nmnl_ht + tilt_ht;
      break;
    case 180:
      pstn_len[0] = nmnl_ht - tilt_ht;
      pstn_len[1] = nmnl_ht + tilt_ht;
      pstn_len[2] = nmnl_ht + tilt_ht;
      break;
    case 240:
      pstn_len[0] = nmnl_ht - tilt_ht;
      pstn_len[1] = nmnl_ht + tilt_ht;
      pstn_len[2] = nmnl_ht + tilt_ht;
      break;
    case 300:
      pstn_len[0] = nmnl_ht + tilt_ht;
      pstn_len[1] = nmnl_ht + tilt_ht;
      pstn_len[2] = nmnl_ht - tilt_ht;
      break;    
  }
}
