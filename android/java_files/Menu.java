package com.example.premal2.turbaflow;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.TextView;

public class Menu extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        getSupportActionBar().hide();
        setContentView(R.layout.activity_menu);
        TextView crowdcontrl=(TextView) findViewById(R.id.crowdcontlbtn);
        crowdcontrl.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                startActivity(new Intent(Menu.this,Crowdcontrol.class));
            }
        });

    }
}
