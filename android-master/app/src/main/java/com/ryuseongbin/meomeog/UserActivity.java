package com.ryuseongbin.meomeog;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.support.v7.app.AlertDialog;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.RadioButton;
import android.widget.RadioGroup;
import android.widget.ScrollView;
import android.widget.TextView;

/**
 * Created by 민지 on 2017-12-05.
 */

public class UserActivity extends AppCompatActivity {
    ScrollView sc;
    TextView tv;
    RadioGroup rg, rg2, rg3, rg4, rg5, rg6, rg7, rg8, rg9, rg10, rg11, rg12, rg13, rg14, rg15;
    RadioButton rb;
    String s;
    SharedPreferences pref;
    SharedPreferences.Editor editor;
    int radioID;
    AlertDialog.Builder al;

    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_user);
        sc = (ScrollView)findViewById(R.id.sc);

        rg = (RadioGroup)findViewById(R.id.RG);
        rg2 = (RadioGroup)findViewById(R.id.rg1);
        rg3 = (RadioGroup)findViewById(R.id.rg2);
        rg4 = (RadioGroup)findViewById(R.id.rg3);
        rg5 = (RadioGroup)findViewById(R.id.rg4);
        rg6 = (RadioGroup)findViewById(R.id.rg5);
        rg7 = (RadioGroup)findViewById(R.id.rg6);
        rg8 = (RadioGroup)findViewById(R.id.rg7);
        rg9 = (RadioGroup)findViewById(R.id.rg8);
        rg10 = (RadioGroup)findViewById(R.id.rg9);
        rg11 = (RadioGroup)findViewById(R.id.rg10);
        rg12 = (RadioGroup)findViewById(R.id.rg11);
        rg13 = (RadioGroup)findViewById(R.id.rg12);
        rg14 = (RadioGroup)findViewById(R.id.rg13);
        rg15 = (RadioGroup)findViewById(R.id.rg14);

        tv = (TextView)findViewById(R.id.textView);
        Button b = (Button)findViewById(R.id.save);

        pref= getSharedPreferences("pref", MODE_PRIVATE);
        editor = pref.edit();

        al = new AlertDialog.Builder(this);

        b.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                // Male/ Female
                radioID = rg.getCheckedRadioButtonId();
                rb = (RadioButton)findViewById(radioID);
                if(rb.isChecked()){

                    s = rb.getText().toString();
                    editor.putString("gender",s);
                }

                // Hansick
                radioID = rg2.getCheckedRadioButtonId();
                rb = (RadioButton)findViewById(radioID);

                if(rb.isChecked()){
                    s = rb.getText().toString();
                    editor.putString("hansick",s);
                }
                //jungsick
                radioID = rg3.getCheckedRadioButtonId();
                rb = (RadioButton)findViewById(radioID);

                if(rb.isChecked()) {
                    s = rb.getText().toString();
                    editor.putString("jungsick", s);
                }
                //gogi
                radioID = rg4.getCheckedRadioButtonId();
                rb = (RadioButton)findViewById(radioID);

                if(rb.isChecked()){
                    s = rb.getText().toString();
                    editor.putString("gogi",s);
                }
                //goongmul
                radioID = rg5.getCheckedRadioButtonId();
                rb = (RadioButton)findViewById(radioID);
                if(rb.isChecked()) {
                    s = rb.getText().toString();
                    editor.putString("goongmul",s);
                }

                //ilsick
                radioID = rg6.getCheckedRadioButtonId();
                rb = (RadioButton)findViewById(radioID);

                if(rb.isChecked()){
                    s = rb.getText().toString();
                    editor.putString("ilsick",s);
                }

                //fastfood
                radioID = rg7.getCheckedRadioButtonId();
                rb = (RadioButton)findViewById(radioID);

                if(rb.isChecked()){
                    s = rb.getText().toString();
                    editor.putString("fastfood",s);
                }
                //boonsick
                radioID = rg8.getCheckedRadioButtonId();
                rb = (RadioButton)findViewById(radioID);

                if(rb.isChecked()){
                    s = rb.getText().toString();
                    editor.putString("boonsick",s);
                }
                //chicken
                radioID = rg9.getCheckedRadioButtonId();
                rb = (RadioButton)findViewById(radioID);

                if(rb.isChecked()){
                    s = rb.getText().toString();
                    editor.putString("chicken",s);
                }

                //pizza
                radioID = rg10.getCheckedRadioButtonId();
                rb = (RadioButton)findViewById(radioID);

                if(rb.isChecked()){
                    s = rb.getText().toString();
                    editor.putString("pizza",s);
                }

                //noodle
                radioID = rg11.getCheckedRadioButtonId();
                rb = (RadioButton)findViewById(radioID);
                if(rb.isChecked()){
                    s = rb.getText().toString();
                    editor.putString("noodle",s);
                }

                //yangsick
                radioID = rg12.getCheckedRadioButtonId();
                rb = (RadioButton)findViewById(radioID);
                if(rb.isChecked()){
                    s = rb.getText().toString();
                    editor.putString("yangsick",s);
                }

                //livefish
                radioID = rg13.getCheckedRadioButtonId();
                rb = (RadioButton)findViewById(radioID);
                if(rb.isChecked()){
                    s = rb.getText().toString();
                    editor.putString("livefish",s);
                }

                //new
                radioID = rg14.getCheckedRadioButtonId();
                rb = (RadioButton)findViewById(radioID);
                if(rb.isChecked()){
                    s = rb.getText().toString();
                    editor.putString("new",s);
                }

                //distance
                radioID = rg15.getCheckedRadioButtonId();
                rb = (RadioButton)findViewById(radioID);
                if(rb.isChecked()){
                    s = rb.getText().toString();
                    editor.putString("distance",s);
                }



                editor.commit();

                //저장된거 값 중 한식, 중식 읽기
                SharedPreferences prefb =getSharedPreferences("pref", MODE_PRIVATE);
                String s ="[저장값 확인]\n한식: " + prefb.getString("hansick","");
                s = s + "중식: " + prefb.getString("jungsick","");
                al.setMessage(s);
                al.setPositiveButton("확인",null);
                AlertDialog all = al.create();
                all.setIcon(R.drawable.ic_menu_send);
                all.show();



            }
        });






    }
}
