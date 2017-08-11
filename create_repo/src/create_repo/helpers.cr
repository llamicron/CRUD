module CreateRepo::Helpers
  def capture_stdout
    out, err, in = Stdio.capture do |io|
      yield
    end
  end
end
