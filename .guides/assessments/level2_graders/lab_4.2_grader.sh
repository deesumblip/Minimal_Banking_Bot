#!/bin/bash
# Lab 4.2 verifies the same deliverable as Lab 4.1: both actions registered in the domain.
# Lab instructs students: main folder (one above level2) -> cd level2 -> activate -> train.
# Grader mirrors that: cd to Codio workspace root (one above level2), then cd level2.
cd /home/codio/workspace
cd level2
exec bash /home/codio/workspace/.guides/assessments/level2_graders/lab_4.1_grader.sh
