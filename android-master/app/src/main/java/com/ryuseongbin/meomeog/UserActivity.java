package com.ryuseongbin.meomeog;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.support.v7.app.AlertDialog;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
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
    EditText et;
    String s;
    SharedPreferences pref;
    SharedPreferences.Editor editor;
    int radioID;
    Intent intent;

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

        et = (EditText)findViewById(R.id.edittext);
        tv = (TextView)findViewById(R.id.textView);
        Button b = (Button)findViewById(R.id.save);

        pref= getSharedPreferences("pref", MODE_PRIVATE);
        editor = pref.edit();
        intent = new Intent(UserActivity.this, MainActivity.class);

        b.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if(et.getText().length() != 0) {
                    String age = et.getText().toString();
                    Log.d("UserAct", age);
                    editor.putString("age", age);
                }

                // Male/ Female
                radioID = rg.getCheckedRadioButtonId();
                if(radioID != -1){
                    rb = (RadioButton)findViewById(radioID);
                    s = rb.getText().toString();
                    editor.putString("gender",s);
                }

                // Hansick
                radioID = rg2.getCheckedRadioButtonId();
                if(radioID != -1){
                    rb = (RadioButton)findViewById(radioID);
                    s = rb.getText().toString();
                    editor.putString("hansick",s);
                }

                //jungsick
                radioID = rg3.getCheckedRadioButtonId();
                if(radioID != -1){
                    rb = (RadioButton)findViewById(radioID);
                    s = rb.getText().toString();
                    editor.putString("jungsick", s);
                }

                //gogi
                radioID = rg4.getCheckedRadioButtonId();
                if(radioID != -1){
                    rb = (RadioButton)findViewById(radioID);
                    s = rb.getText().toString();
                    editor.putString("gogi",s);
                }

                //goongmul
                radioID = rg5.getCheckedRadioButtonId();
                if(radioID != -1){
                    rb = (RadioButton)findViewById(radioID);
                    s = rb.getText().toString();
                    editor.putString("goongmul",s);
                }

                //ilsick
                radioID = rg6.getCheckedRadioButtonId();
                if(radioID != -1){
                    rb = (RadioButton)findViewById(radioID);
                    s = rb.getText().toString();
                    editor.putString("ilsick",s);
                }

                //fastfood
                radioID = rg7.getCheckedRadioButtonId();
                if(radioID != -1){
                    rb = (RadioButton)findViewById(radioID);
                    s = rb.getText().toString();
                    editor.putString("fastfood",s);
                }

                //boonsick
                radioID = rg8.getCheckedRadioButtonId();
                if(radioID != -1){
                    rb = (RadioButton)findViewById(radioID);
                    s = rb.getText().toString();
                    editor.putString("boonsick",s);
                }

                //chicken
                radioID = rg9.getCheckedRadioButtonId();
                if(radioID != -1){
                    rb = (RadioButton)findViewById(radioID);
                    s = rb.getText().toString();
                    editor.putString("chicken",s);
                }

                //pizza
                radioID = rg10.getCheckedRadioButtonId();
                if(radioID != -1){
                    rb = (RadioButton)findViewById(radioID);
                    s = rb.getText().toString();
                    editor.putString("pizza",s);
                }

                //noodle
                radioID = rg11.getCheckedRadioButtonId();
                if(radioID != -1){
                    rb = (RadioButton)findViewById(radioID);
                    s = rb.getText().toString();
                    editor.putString("noodle",s);
                }

                //yangsick
                radioID = rg12.getCheckedRadioButtonId();
                if(radioID != -1){
                    rb = (RadioButton)findViewById(radioID);
                    s = rb.getText().toString();
                    editor.putString("yangsick",s);
                }

                //livefish
                radioID = rg13.getCheckedRadioButtonId();
                if(radioID != -1){
                    rb = (RadioButton)findViewById(radioID);
                    s = rb.getText().toString();
                    editor.putString("livefish",s);
                }

                //new
                radioID = rg14.getCheckedRadioButtonId();
                if(radioID != -1){
                    rb = (RadioButton)findViewById(radioID);
                    s = rb.getText().toString();
                    editor.putString("new",s);
                }

                //distance
                radioID = rg15.getCheckedRadioButtonId();
                if(radioID != -1){
                    rb = (RadioButton)findViewById(radioID);
                    s = rb.getText().toString();
                    editor.putString("distance",s);
                }

                editor.commit();

                startActivity(intent);
                finish();
            }
        });



    }
}
