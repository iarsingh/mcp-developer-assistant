from mcpx.progression import mcp_dev

def test_mcp_dev_needs_approval():
    out = mcp_dev("fs.read", {"path": "/etc", "apply": True}, approved=False)
    assert out["needs_approval"] is True
    assert out["applied"] is False

