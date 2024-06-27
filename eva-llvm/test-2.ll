; ModuleID = 'test.bc'
source_filename = "test.cpp"
target datalayout = "e-m:o-i64:64-i128:128-n32:64-S128"
target triple = "arm64-apple-macosx14.0.0"

define i32 @main() {
  ret i32 100
}
